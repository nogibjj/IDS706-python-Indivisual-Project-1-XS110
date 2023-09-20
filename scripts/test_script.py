import unittest
import subprocess

class TestScriptExecution(unittest.TestCase):
    def test_script_runs_without_errors(self):
        try:
            # Run script.py using subprocess
            result = subprocess.run(["python", "scripts/script.py"], capture_output=True, text=True, check=True)

            # Check if the return code is 0 (indicating success)
            self.assertEqual(result.returncode, 0)

            # check the script's output 
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            self.fail(f"script.py raised an error: {e}")

if __name__ == '__main__':
    unittest.main()
