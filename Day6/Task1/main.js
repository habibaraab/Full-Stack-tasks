 function updateLights() {
            const val = document.getElementById('input').value;
            const l1 = document.getElementById('light1');
            const l2 = document.getElementById('light2');
            const l3 = document.getElementById('light3');

            light1.className = 'circle';
            light2.className = 'circle';
            light3.className = 'circle';

            switch (val) {
                case '1':
                    l1.classList.add('light-blue'); 
                    break;
                case '2':
                    l2.classList.add('light-yellow'); 
                    break;
                case '3':
                    l3.classList.add('light-red');
                    break;
                
            }
        }
          const num = document.getElementById('input');
        num.addEventListener('input', updateLights);



        
    