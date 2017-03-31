import argparse


from toil.common import Toil
from toil.job import Job


def parent(job):
    for i in range(10):
        job.addChildJobFn(smallJob, memory="1.0G")
    for i in range(10):
        job.addChildJobFn(largeJob, memory="3.0G")

def smallJob(job):
    job.logToMaster("Running small job")

def largeJob(job):
    job.logToMaster("Running large job")

def main():
    parser = argparse.ArgumentParser()
    Job.Runner.addToilOptions(parser)
    options = parser.parse_args()
    with Toil(options) as toil:
        toil.start(Job.wrapJobFn(parent))

if __name__ == "__main__":
    main()
                   
