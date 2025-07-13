 const calculateBtn = document.getElementById('calculateBtn');
        const out = document.getElementById('output');

        calculateBtn.addEventListener('click', function() {
            const num = [];
            
            for (let i = 1; i <= 5; i++) {
                const inputElement = document.getElementById('num' + i);
                num.push(Number(inputElement.value));
            }

           const sq = [];
            for (let i = 0; i < num.length; i++) {
                const sqq = num[i] * num[i];
                sq.push(sqq);
            }
            out.textContent = sq.join(', ');


        });

    




