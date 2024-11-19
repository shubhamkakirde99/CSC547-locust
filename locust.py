from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    @task
    def my_task(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)
    host = "http://ac982e05352d34ce382ba80229a5ac0c-1217945811.us-east-1.elb.amazonaws.com/"
    min_wait = 1000
    max_wait = 2000
    stop_timeout = 10
