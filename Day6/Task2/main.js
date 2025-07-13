 function ch() {
            const input = document.getElementById('input');
            const out = document.getElementById('out');
            const num = Number(input.value);

            if (input.value === '' || isNaN(num)) {
                out.textContent = '""';
                return;
            }
            let result = '';
            if (num % 15 === 0) {
                result = 'fizz buzz';
            } else if (num % 3 === 0) {
                result = 'fizz';
            } else if (num % 5 === 0) {
                result = 'buzz';
            } else {
                result = 'none';
            }
            out.textContent = `"${result}"`;
        }
           const out = document.getElementById('out');
            num.addEventListener('out',ch);
