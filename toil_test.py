from toil.job import Job
import os
import argparse
import tempfile
from toil.common import setupToil

def writeJob(job):
    #tmpFile = tempfile.mkstemp(dir=job.fileStore.getLocalTempDir())
    testPath = os.path.join(job.fileStore.getLocalTempDir(), "test.txt")
    os.system("touch %s" % testPath)
    job.addFollowOnJobFn(readJob, job.fileStore.writeGlobalFile(testPath))
def readJob(job, fileID):
    job.fileStore.readGlobalFile(fileID)

def main():
    parser = argparse.ArgumentParser()
    Job.Runner.addToilOptions(parser)
    args = parser.parse_args()
    rootJob = Job.wrapJobFn(writeJob)
    with setupToil(args) as (config, batchSystem, jobStore):
	Job.Runner.start(rootJob, args, config, batchSystem, jobStore)

if __name__ == "__main__":
    main()
    
