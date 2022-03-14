import re
import shlex
import asyncio
from os.path import basename, join, exists
from typing import Tuple, Optional
from TeamIndia import LOGGER, TEMP_DOWNLOAD_DIRECTORY



async def runcmd(cmd: str) -> Tuple[str, str, int, int]:
    """ run command in terminal """
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(*args,
                                                   stdout=asyncio.subprocess.PIPE,
                                                   stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    return (stdout.decode('utf-8', 'replace').strip(),
            stderr.decode('utf-8', 'replace').strip(),
            process.returncode,
            process.pid)


async def take_screen_shot(video_file: str, duration: int, path: str = '') -> Optional[str]:
    """ take a screenshot """
    LOGGER.info('[[[Extracting a frame from %s ||| Video duration => %s]]]', video_file, duration)
    ttl = duration // 2
    thumb_image_path = path or join(TEMP_DOWNLOAD_DIRECTORY, f"{basename(video_file)}.jpg")
    command = f'''ffmpeg -ss {ttl} -i "{video_file}" -vframes 1 "{thumb_image_path}"'''
    err = (await runcmd(command))[1]
    if err:
        LOGGER.error(err)
    return thumb_image_path if exists(thumb_image_path) else None
