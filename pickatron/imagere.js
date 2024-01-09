// Define the words and images
const words = [
    { word: 'apple', img: 'apple.jpg' },
    { word: 'banana', img: 'banana.jpg' },
    { word: 'orange', img: 'orange.jpg' },
    { word: 'grape', img: 'grape.jpg' }
  ];
  
  // Get random word and set the image sources
  const randomWord = words[Math.floor(Math.random() * words.length)];
  document.getElementById('word').textContent = randomWord.word;
  document.querySelectorAll('#images img').forEach((img, index) => {
    img.src = words[index].img;
  });
  
  // Add event listener to check button
document.getElementById('check-btn').addEventListener('click', () => {
    const selectedImg = document.querySelector('#images img.selected');
    if (!selectedImg) {
      document.getElementById('result').textContent = 'Please select an image';
      return;
    }
    if (selectedImg.src.endsWith(randomWord.img)) {
      document.getElementById('result').textContent = 'Correct!';
    } else {
      document.getElementById('result').textContent = 'Incorrect!';
    }
  });
  
  // Add event listener to images
  document.querySelectorAll('#images img').forEach(img => {
    img.addEventListener('click', () => {
      document.querySelectorAll('#images img').forEach(img => {
        img.classList.remove('selected');
      });
      img.classList.add('selected');
    });
  });