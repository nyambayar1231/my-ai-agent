import os


def get_files_info(working_directory: str, directory: str= ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    common_path = os.path.commonpath([working_dir_abs, target_dir])
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    print("target dir path:", target_dir)
    print("common dir path:", common_path)
    print("valid target dir:", valid_target_dir)
    if not valid_target_dir:
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    return "hello"
