from toil.job import Job
from toil.common import Toil
import argparse

def job1(job):
    job.fileStore.logToMaster("working")

def main():
    parser = argparse.ArgumentParser()
    Job.Runner.addToilOptions(parser)
    args = parser.parse_args()
    with Toil(args) as toil:
        toil.start(Job.wrapJobFn(job1))

if __name__ == "__main__":
    main()
