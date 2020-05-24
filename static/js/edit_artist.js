// var form = document.querySelector("form");
// form.addEventListener("change", function () {
// 	alert("Hi!");
// });

document.getElementById("edit-artist-form").onsubmit = (event) => {
	event.preventDefault();
	const artist_id = window.location.pathname.split("/")[2];
	console.log(artist_id);
	const genres = document.getElementById("genres");
	let genres_list = [];
	for (let i = 0; i < genres.selectedOptions.length; i++) {
		genres_list.push(genres.selectedOptions[i].value);
	}

	const name = document.getElementById("name");

	const city = document.getElementById("city");

	const state = document.getElementById("state");

	const phone = document.getElementById("phone");
	const facebook_link = document.getElementById("facebook_link");
	console.log(genres);
	fetch("/artists/" + artist_id + "/edit", {
		method: "POST",
		body: JSON.stringify({
			id: artist_id,
			name: name.value,
			genres: genres_list,
			city: city.value,
			state: state.value,
			facebook_link: facebook_link.value,
			phone: phone.value,
		}),
		headers: {
			"Content-Type": "application/json",
		},
	}).then((response) => {
		window.location.replace("/artists/" + artist_id);
	});
};
