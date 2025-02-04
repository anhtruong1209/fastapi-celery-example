"""Celery Tasks."""
import random
import time

from celery_app import celery_app

@celery_app.task(bind=True)
def long_task(self):
    """Background task that runs a long function with progress reports."""
    verb = ["Starting up", "Booting", "Repairing", "Loading", "Checking"]
    adjective = ["master", "radiant", "silent", "harmonic", "fast"]
    noun = ["solar array", "particle reshaper", "cosmic ray", "orbiter", "bit"]
    message = ""
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = f"{random.choice(verb)} {random.choice(adjective)} " \
                f"{random.choice(noun)}"
        self.update_state(state="PROGRESS",
                          meta={
                              "current": i,
                              "total": total,
                              "status": message,
                          })
        time.sleep(1)
    return {
        "current": 100,
        "total": 100,
        "status": "Task completed!",
        "result": 42,
    }

@celery_app.task(bind=True)
def long_task_2(self):
    """Background task that runs a long function with progress reports."""
    verb = ["Starting up", "Booting", "Repairing", "Loading", "Checking"]
    adjective = ["master", "radiant", "silent", "harmonic", "fast"]
    noun = ["solar array", "particle reshaper", "cosmic ray", "orbiter", "bit"]
    message = ""
    total = random.randint(4,10)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = f"{random.choice(verb)} {random.choice(adjective)} " \
                f"{random.choice(noun)}"
        self.update_state(state="PROGRESS",
                          meta={
                              "current": i,
                              "total": total,
                              "status": message,
                          })
        time.sleep(1)
    return {
        "current": 100,
        "total": 100,
        "status": "Task hoàn thành!",
        "result": 100,
    }
