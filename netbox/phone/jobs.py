from netbox.jobs import JobRunner
from core.models import Job


class MyHousekeepingJob(JobRunner):
    class Meta:
        name = "Housekeeping"

    def run(self, *args, **kwargs):
        
        print("Housekeeping")