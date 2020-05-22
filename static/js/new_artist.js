document.getElementById("new-artist-form").onsubmit = function (e) {
	e.preventDefault();
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

	fetch("/artists/create", {
		method: "POST",
		body: JSON.stringify({
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
		console.log(response);
		window.location.replace("/");
	});
};
