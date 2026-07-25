import subprocess

from src.config.application_paths import APPLICATION_PATHS


class ApplicationLauncher:

    def open_application(self, command):

        command = command.lower().strip()

        for app_name, app_path in APPLICATION_PATHS.items():

            if app_name in command:

                try:
                    subprocess.Popen(app_path)

                    return f"Opening {app_name}."

                except Exception as e:

                    return f"Unable to open {app_name}. Error: {e}"

        return None