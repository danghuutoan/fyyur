updateVenue = (event) => {
	event.preventDefault();

	const genres = document.getElementById("genres");
	let genres_list = [];
	for (let i = 0; i < genres.selectedOptions.length; i++) {
		genres_list.push(genres.selectedOptions[i].value);
	}

	const name = document.getElementById("name").value;

	const city = document.getElementById("city").value;

	const state = document.getElementById("state").value;

	const phone = document.getElementById("phone").value;
	const facebook_link = document.getElementById("facebook_link").value;

	console.log(name);
	console.log(city);
	console.log(state);
	console.log(phone);
	console.log(facebook_link);
	console.log(genres);

	if (window.location.pathname === "/venues/create") {
		fetch("/venues/create", {
			method: "POST",
			body: JSON.stringify({
				name: name,
				genres: genres_list,
				city: city,
				state: state,
				facebook_link: facebook_link,
				phone: phone,
			}),
			headers: {
				"Content-Type": "application/json",
			},
		}).then((response) => {
			window.location.replace("/");
		});
	} else {
		fetch(window.location.pathname, {
			method: "POST",
			body: JSON.stringify({
				name: name,
				genres: genres_list,
				city: city,
				state: state,
				facebook_link: facebook_link,
				phone: phone,
			}),
			headers: {
				"Content-Type": "application/json",
			},
		}).then((response) => {
			const artist_id = window.location.pathname.match(
				"/venues/(?<id>\\d+)/edit$"
			)[1];
			console.log(artist_id);
			if (artist_id) {
				window.location.replace("/venues/" + artist_id);
			} else {
				window.location.replace("/");
			}
			// window.location.replace("/");
		});
	}
	// // const string = "/venue/19/edit1";
	// // // const string = "/venue/create";
	//
};
