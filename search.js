async function search(query) {
  const response = await fetch(`http://127.0.0.1:5000/search?query=${query}`);
  const data = await response.json();
  return data;
}

const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const searchResults = document.getElementById("search-results");

searchForm.addEventListener("submit", (event) => {
  // Prevent the form from submitting and refreshing the page
  event.preventDefault();

  // Get container element
  const container = document.querySelector('#container');
  const container2 = document.querySelector('#container2');
  const temp = document.getElementById('temp');

  // Remove the extra space (created from below)
  if(temp) {
    temp.remove();
  }
  
  // Remove container element
  if(container) {
    container.remove();
    container2.remove();
  }
  
  // Get the search query from the input field
  const query = searchInput.value;

  // Clear the search results list
  searchResults.innerHTML = "";

  // Search the database and add the results to the list
  search(query).then((data) => {
    const combined = data["desala"].concat(data["gen"]);
    // Shuffle the combined array
    for (let i = combined.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [combined[i], combined[j]] = [combined[j], combined[i]];
    }
    // Iterate over the combined array
    for (const item of combined) {
        const li = document.createElement("li");
        li.textContent = item;
        // Check if the item is from the "gen" array
        if (data["gen"].includes(item)) li.style.color = "#0f0";
        searchResults.appendChild(li);
    }
  });

  // Add some space for the tip button...
  var div = document.createElement("div");
  div.style.width = "100%";
  div.style.height = "36px";
  div.id = "temp";

  document.body.appendChild(div);

});
