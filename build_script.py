import os
import sys
import subprocess

def main():
    print("Starting Flet build process...")
    
    # Устанавливаем переменные окружения
    env = os.environ.copy()
    env['PYTHONIOENCODING'] = 'utf-8'
    env['FORCE_COLOR'] = '0'
    env['TERM'] = 'dumb'
    
    try:
        # Запускаем flet build windows
        result = subprocess.run([
            sys.executable, '-m', 'flet', 'build', 'windows'
        ], 
        cwd='src',
        env=env,
        capture_output=True,
        text=True,
        encoding='utf-8'
        )
        
        print("STDOUT:", result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
            
        return result.returncode
        
    except Exception as e:
        print(f"Error during build: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
