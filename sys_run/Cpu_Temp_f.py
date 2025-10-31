import os
import platform
import subprocess
import psutil

def get_cpu_temperature():
    try:
        if platform.system().lower() == 'linux':
            # Raspberry Pi uses vcgencmd command to get CPU temperature
            process = subprocess.Popen(['vcgencmd', 'measure_temp'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            output, error = process.communicate()

            if process.returncode == 0:
                temperature_str = output.decode('utf-8').strip().replace('temp=', '').replace("'C", '')
                return float(temperature_str)
            else:
                raise Exception(f"Error executing vcgencmd: {error.decode('utf-8')}")

        else:
            raise Exception("Unsupported platform. This script is designed for Linux-based systems.")

    except Exception as e:
        print(f"Error: {e}")
        return None
