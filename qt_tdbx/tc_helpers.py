import os
import shutil
from multiprocessing import Pool, current_process
from typing import Dict

from tc_python import System, start_api_server, stop_api_server, LoggingPolicy, SetUp

from . import variables as v


def get_new_system(parameters: Dict[str, str]) -> System:
    """Generate a new TC System with given parameters."""
    shutil.rmtree(v.cache_folder)
    shutil.copytree(v.temp_folder, v.cache_folder)

    new_system = v.init_system
    for parameter, new_value in parameters.items():
        new_system = new_system.set_ges_parameter(parameter, new_value)

    return new_system


def initializer() -> None:
    """Initialize the pool with TC setups. Only works for Unix platform."""
    pid = current_process().pid
    v.cache_folder = os.path.join(os.getcwd(), 'cache', str(pid))
    v.temp_folder = os.path.join(os.getcwd(), 'temp', str(pid))
    for folder in [v.cache_folder, v.temp_folder]:
        if os.path.exists(folder):
            shutil.rmtree(folder)

    start_api_server(logging_policy=LoggingPolicy.NONE)
    v.init_system = (
        SetUp()
            .set_cache_folder(v.cache_folder)
            .set_ges_version(5)
            .select_user_database_and_elements(v.tdbx_file, v.elements)
            .get_system()
    )
    shutil.copytree(v.cache_folder, v.temp_folder)


def clean_up_single(index: int) -> None:
    stop_api_server()
    print(f'TC-Python #{index} is closed.')


def clean_up(pool: Pool, n_procs: int) -> None:
    """Clean up the pool."""
    pool.map(clean_up_single, range(n_procs))
    pool.terminate()
    shutil.rmtree(os.path.join(os.getcwd(), 'cache'))
    shutil.rmtree(os.path.join(os.getcwd(), 'temp'))
