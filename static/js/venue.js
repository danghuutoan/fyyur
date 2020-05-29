handleVenueDelele = (venue_id) => {
	fetch("/venues/" + venue_id, {
		method: "DELETE",
		body: {},
	}).then((response) => {
		console.log(response);
		window.location.replace("/venues");
	});
};
