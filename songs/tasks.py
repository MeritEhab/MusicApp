from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from songs.utils import save_song

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/10')),
    name="task_save_song",
    ignore_result=True
)
def task_save_song():

    save_song()
    logger.info("Song Saved")