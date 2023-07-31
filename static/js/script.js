// document.addEventListener('DOMContentLoaded', () => {
  let autoScore = 0;
  let manualScore = 0;
  let selectedLevel = null;

  // Auto Stage
  function calculateAutoScore() {
    const autoGoals = parseInt(document.getElementById('autoGoals').value);
    autoScore = autoGoals * 4; // Each goal scores 4 points
    document.getElementById('autoScore').innerText = `Auto Score: ${autoScore}`;
  }

  // Manual Stage
  function calculateManualScore() {
    const manualGoals = parseInt(document.getElementById('manualGoals').value);
    manualScore = manualGoals * 2; // Each goal scores 2 points
    document.getElementById('manualScore').innerText = `Manual Score: ${manualScore}`;
  }

  // Climbing Level
  const levelSpans = document.querySelectorAll('.climbing-level span');
  levelSpans.forEach(span => {
    span.addEventListener('click', selectLevel);
  });

  function selectLevel(event) {
    const clickedLevel = event.target.dataset.level;
    selectedLevel = clickedLevel;
    document.getElementById('selectedLevel').innerText = `Selected Level: ${selectedLevel}`;

    // Remove the "selected" class from all spans
    levelSpans.forEach(span => {
      span.classList.remove('selected');
    });

    // Add the "selected" class to the clicked span
    event.target.classList.add('selected');
  }

  // Save Data
  const saveDataButton = document.getElementById('saveData');
  saveDataButton.addEventListener('click', saveData);

  function saveData() {
    const teamNumber = document.getElementById('teamNumber').value.trim();
    if (!teamNumber) {
      alert('Please enter a valid Team Number.');
      return;
    }

    const totalBallsThrown = parseInt(document.getElementById('autoBallsThrown').value) + parseInt(document.getElementById('manualBallsThrown').value);
    const totalGoals = parseInt(document.getElementById('autoGoals').value) + parseInt(document.getElementById('manualGoals').value);
    const totalScore = autoScore + manualScore;

    // Show the "Correct" symbol in the modal window
    const modal = document.getElementById('modal');
    const modalContent = document.querySelector('.modal-content');

    // Clear existing content before adding new "Correct" symbol
    modalContent.innerHTML = '';

    const correctSymbol = document.createElement('span');
    correctSymbol.classList.add('correct-symbol');
    correctSymbol.innerHTML = '&#10004;';
    modalContent.appendChild(correctSymbol);

    // Show the modal window with blur effect
    modal.style.display = 'block';

    // sendDataToServer(teamNumber, totalBallsThrown, totalGoals, totalScore, selectedLevel);
  }

  function submit() {
    const data = {
      team_num: 123,
      game_id: 0,
      auto_shoots: 6,
      auto_goals: 7,
      teleop_shoots: 8,
      teleop_goals: 9,
      climb_score: 10,
      foul: 0
    };

    // You can use JavaScript fetch API to send the data to the server
    fetch('/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      console.log('Data saved on the server:', data);
      // You can show a success message to the user if needed.
    })
    .catch(error => {
      console.error('Error saving data:', error);
      // You can show an error message to the user if something goes wrong.
    });
  }
// });
