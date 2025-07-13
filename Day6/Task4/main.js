   const gameArea = document.getElementById('gameArea');
        const questionBox = document.getElementById('question-box');
        const resultArea = document.getElementById('resultArea');
        const resultImage = document.getElementById('resultImage');
        const resultName = document.getElementById('resultName');
        const yesBtn = document.getElementById('yesBtn');
        const noBtn = document.getElementById('noBtn');
        const resetBtn = document.getElementById('resetBtn');

        let cur = 1;
        const questions = {
            fly: "Do you fly?",
            wild: "Are You Wild?",
            sea: "Do you live under sea?"
        };
        const results = {
            eagle: { name: "Eagle", image: "images/6057813250b001d3b8ef03df0051c901.jpg" },
            parrot: { name: "Parrot", image: "images/images.jpeg" },
            shark: { name: "Shark", image: "https://img.icons8.com/plasticine/200/shark.png" },
            dolphin: { name: "Dolphin", image: "images/png-transparent-cartoon-dolphin-lovely-dolphin-friend-thumbnail.png" },
            lion: { name: "Lion", image: "https://img.icons8.com/plasticine/200/lion.png" },
            cat: { name: "Cat", image: "https://img.icons8.com/plasticine/200/cat.png" }
        };

        function startGame() {
            cur = 1;
            questionBox.textContent = questions.fly;
            gameArea.classList.remove('hidden');
            resultArea.classList.add('hidden');
            resetBtn.classList.add('hidden');
        }

        function handleAnswer(answer) {
            if (cur === 1) {
                if (answer === 'yes') {
                    cur = 'fly_wild';
                    questionBox.textContent = questions.wild;
                } else { 
                    cur = 'sea';
                    questionBox.textContent = questions.sea;
                }
            } 
            else if (cur === 'fly_wild') {
                if (answer === 'yes') showResult(results.eagle);
                else showResult(results.parrot);
            }
            else if (cur === 'sea') {
                if (answer === 'yes') {
                    cur = 'sea_wild';
                    questionBox.textContent = questions.wild;
                } else { // no
                    cur = 'land_wild';
                    questionBox.textContent = questions.wild;
                }
            }
            else if (cur === 'sea_wild') {
                if (answer === 'yes') showResult(results.shark);
                else showResult(results.dolphin);
            }
            else if (cur === 'land_wild') {
                if (answer === 'yes') showResult(results.lion);
                else showResult(results.cat);
            }
        }

        function showResult(result) {
            resultImage.src = result.image;
            resultName.textContent = result.name;
            gameArea.classList.add('hidden');
            resultArea.classList.remove('hidden');
            resetBtn.classList.remove('hidden');
        }

        yesBtn.addEventListener('click', () => handleAnswer('yes'));
        noBtn.addEventListener('click', () => handleAnswer('no'));
        resetBtn.addEventListener('click', startGame);