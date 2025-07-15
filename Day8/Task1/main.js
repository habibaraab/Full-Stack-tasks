 let movingWindow;
        let moveInterval;
        let isStopped = false;
        let x_pos = 0;
        let y_pos = 0;
        
        const x_speed = 5;
        const y_speed = 5;

        const windowWidth = 30;
        const windowHeight = 30;

        function animateWindow() {
          
            if (isStopped) {
                return;
            }

            if (!movingWindow || movingWindow.closed) {
                stopAnimation();
                return;
            }

            x_pos += x_speed;
            y_pos += y_speed;

            if (x_pos > screen.width || y_pos > screen.height) {
                x_pos = 0;
                y_pos = 0;
            }

            movingWindow.moveTo(x_pos, y_pos);
            movingWindow.focus();
        }

        function stopAnimation() {
            isStopped = true;
            clearInterval(moveInterval);
        }

        function startOnLoad() {
            movingWindow = window.open('', 'flyingWindow', `width=${windowWidth},height=${windowHeight}`);

            if (movingWindow) {
                movingWindow.document.write('<h3 style="font-family: sans-serif; text-align: center;">Moving</h3>');
                moveInterval = setInterval(animateWindow, 20);
            } 
        }

        document.getElementById('stopButton').addEventListener('click', stopAnimation);

        window.onload = startOnLoad;