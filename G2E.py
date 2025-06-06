import os
import subprocess
import sys

def check_node():
    try:
        node_version = subprocess.check_output(['node', '-v'], text=True).strip()
        print(f'Node.js 버전 {node_version} 감지됨.')
    except Exception:
        print('Node.js가 설치되어 있지 않습니다. 설치 후 다시 시도하세요.')
        sys.exit(1)

def parse_and_write(text):
    lines = text.splitlines()
    folder_name = lines[0].strip()
    if not folder_name:
        print("폴더 이름이 비어있습니다!")
        sys.exit(1)
    os.makedirs(folder_name, exist_ok=True)

    current_file = None
    content_lines = []

    for line in lines[1:]:
        line = line.rstrip('\r\n')
        if line.startswith('[') and line.endswith(']'):
            if current_file is not None:
                filepath = os.path.join(folder_name, current_file)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(content_lines))
                print(f"'{current_file}' 파일 생성 완료!")
            current_file = line[1:-1].strip()
            content_lines = []
        elif line == 'END':
            if current_file is not None:
                filepath = os.path.join(folder_name, current_file)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(content_lines))
                print(f"'{current_file}' 파일 생성 완료!")
            break
        else:
            content_lines.append(line)

    return folder_name

def npm_install_and_start(folder_name):
    print("\nnpm install 실행 중...")
    try:
        subprocess.run(['npm.cmd', 'install'], cwd=folder_name, check=True)
        print("✅ npm install 완료!")
    except subprocess.CalledProcessError:
        print("❌ npm install 실패! 수동으로 시도해봐요.")
        return
    except FileNotFoundError:
        print("❌ 'npm' 명령어를 찾을 수 없습니다. Node.js가 PATH에 제대로 등록됐는지 확인해줘요.")
        return

    print("🚀 Electron 앱 자동 실행 중...")
    try:
        subprocess.run(['npm.cmd', 'start'], cwd=folder_name, check=True)
    except subprocess.CalledProcessError:
        print("❌ Electron 실행 실패! 수동으로 'npm start' 해보세요.")


def main():
    print("복사한 코드를 붙여넣고, 끝에 'END' 입력 후 엔터 누르세요:")
    input_lines = []
    while True:
        line = input()
        input_lines.append(line)
        if line.strip() == 'END':
            break

    input_text = '\n'.join(input_lines)
    folder_name = parse_and_write(input_text)
    print(f"\n'{folder_name}' 폴더에 파일 생성 완료!")

    check_node()
    npm_install_and_start(folder_name)

if __name__ == '__main__':
    main()
