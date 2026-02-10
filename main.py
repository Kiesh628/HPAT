import streamlit as st

def main():
    st.title('test')
    return

if __name__ == "__main__":
    if st.runtime.exists(): #type: ignore
        main()
    else:
        import sys
        import os
        import subprocess
        cmd = [sys.executable, "-m", "streamlit", "run", os.path.abspath(__file__)]
        subprocess.run(cmd)