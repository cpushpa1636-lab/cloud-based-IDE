import streamlit as st
import subprocess
import os
import tempfile

st.title("Cloud IDE")

code = st.text_area("Enter your Python code:", height=300)

if st.button("Run Code"):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".py") as tmp:
            tmp.write(code.encode())
            tmp_path = tmp.name

        result = subprocess.run(
            ["python", tmp_path],
            capture_output=True,
            text=True,
            timeout=5
        )

        output = result.stdout if result.stdout else result.stderr
        st.text_area("Output:", output, height=200)

        os.remove(tmp_path)

    except Exception as e:
        st.error(str(e))
