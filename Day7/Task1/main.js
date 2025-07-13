        const studentForm = document.getElementById('studentForm');
        const studentName = document.getElementById('studentName');
        const studentAge = document.getElementById('studentAge');
        const nameError = document.getElementById('nameError');
        const ageError = document.getElementById('ageError');
        const table = document.getElementById('tableBody');

        let student = [];
        let idCount = 1;

        studentForm.addEventListener('submit', function(event) {
            event.preventDefault();

            const name = studentName.value;
            const age = studentAge.value;
            let isValid = true;
            
          
            if (name.length <= 3) {
                nameError.textContent = 'Student name must be > 3 characters.';
                isValid = false;
            } else {
                nameError.textContent = '';
            }

            
            if (age < 18) {
                ageError.textContent = 'Age must be >= 18.';
                isValid = false;
            } else {
                ageError.textContent = '';
            }

            if (isValid) {
                const newStudent = {
                    id: idCount,
                    name: name,
                    age: Number(age)
                };
                idCount++;
                student.push(newStudent);
                addTable();
                studentForm.reset(); 
                studentName.focus();
            }
        });

        function addTable() {
            table.innerHTML = ''; 

            student.forEach(student => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${student.id}</td>
                    <td>${student.name}</td>
                    <td>${student.age}</td>
                    <td><button class="remove-btn" data-id="${student.id}">Remove</button></td>
                `;
                table.appendChild(row);
            });
        }
        
        table.addEventListener('click', function(event) {
            if (event.target.classList.contains('remove-btn')) {
                const idToRemove = Number(event.target.dataset.id);
                student = student.filter(student => student.id !== idToRemove);
                addTable();
            }
        });
