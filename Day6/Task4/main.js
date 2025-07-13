   const gameArea = document.getElementById('gameArea');
        const questionBox = document.getElementById('question-box');
        const resultArea = document.getElementById('resultArea');
        const resultImage = document.getElementById('resultImage');
        const resultName = document.getElementById('resultName');
        const yesBtn = document.getElementById('yesBtn');
        const noBtn = document.getElementById('noBtn');
        const resetBtn = document.getElementById('resetBtn');

        let currentStage = 1;
        const questions = {
            fly: "Do you fly?",
            wild: "Are You Wild?",
            sea: "Do you live under sea?"
        };
        const results = {
            eagle: { name: "Eagle", image: "https://img.icons8.com/plasticine/200/eagle.png" },
            parrot: { name: "Parrot", image: "https://img.icons8.com/plasticine/200/parrot.png" },
            shark: { name: "Shark", image: "https://img.icons8.com/plasticine/200/shark.png" },
            dolphin: { name: "Dolphin", image: "https://img.icons8.com/plasticine/200/dolphin.png" },
            lion: { name: "Lion", image: "https://img.icons8.com/plasticine/200/lion.png" },
            cat: { name: "Cat", image: "https://img.icons8.com/plasticine/200/cat.png" }
        };

        function startGame() {
            currentStage = 1;
            questionBox.textContent = questions.fly;
            gameArea.classList.remove('hidden');
            resultArea.classList.add('hidden');
            resetBtn.classList.add('hidden');
        }

        function handleAnswer(answer) {
            if (currentStage === 1) {
                if (answer === 'yes') {
                    currentStage = 'fly_wild';
                    questionBox.textContent = questions.wild;
                } else { 
                    currentStage = 'sea';
                    questionBox.textContent = questions.sea;
                }
            } 
            else if (currentStage === 'fly_wild') {
                if (answer === 'yes') showResult(results.eagle);
                else showResult(results.parrot);
            }
            else if (currentStage === 'sea') {
                if (answer === 'yes') {
                    currentStage = 'sea_wild';
                    questionBox.textContent = questions.wild;
                } else { // no
                    currentStage = 'land_wild';
                    questionBox.textContent = questions.wild;
                }
            }
            else if (currentStage === 'sea_wild') {
                if (answer === 'yes') showResult(results.shark);
                else showResult(results.dolphin);
            }
            else if (currentStage === 'land_wild') {
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