from locust import HttpUser, task


class QuickstartUser(HttpUser):
    @task
    def get_base(self):
        self.client.get("/")
