import re

with open('latest1.html', 'r') as f:
    content = f.read()

# Fix the event listener to not be 'once: true' because we want it to close on every click outside
content = re.sub(
    r"window\.addEventListener\('click', globalHideDropdown, \{ once: true \}\);",
    r"window.addEventListener('click', globalHideDropdown);",
    content
)

with open('latest1.html', 'w') as f:
    f.write(content)
