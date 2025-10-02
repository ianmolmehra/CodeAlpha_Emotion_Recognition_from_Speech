const fileInput = document.getElementById('audio-file');
const btn = document.getElementById('predict-btn');
const resultCard = document.getElementById('result');
const emotionP = document.getElementById('emotion');

btn.addEventListener('click', async () => {
  if (!fileInput.files.length) {
    alert('Please choose an audio file (wav/mp3).');
    return;
  }
  const file = fileInput.files[0];
  const fd = new FormData();
  fd.append('audio', file);
  btn.disabled = true; btn.textContent = 'Predicting...';
  try {
    const res = await fetch('/predict', { method: 'POST', body: fd });
    const data = await res.json();
    if (data.error) {
      alert('Error: ' + (data.details||data.error));
    } else {
      emotionP.textContent = data.emotion;
      resultCard.classList.remove('hidden');
    }
  } catch (e) {
    alert('Request failed: ' + e.message);
  } finally {
    btn.disabled = false; btn.textContent = 'Predict Emotion';
  }
});
