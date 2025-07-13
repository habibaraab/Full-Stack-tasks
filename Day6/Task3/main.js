   const outt = document.getElementById('out');
 function find() {
            const text = document.getElementById('input').value;
            const letter = document.getElementById('letter').value;
              const outt = document.getElementById('out');
            if (text === '' || letter === '') {
                outt.textContent = '[]';
                return;
            }

            const arr = [];
            const lowerCaseLetter = letter.toLowerCase();
            for (let i = 0; i < text.length; i++) {
                if (text[i].toLowerCase() === lowerCaseLetter) {
                    arr.push(i);
                }
            }

            outt.textContent = JSON.stringify(arr);
        }
                    outt.addEventListener('out',find());
        

        