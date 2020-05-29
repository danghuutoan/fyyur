handleArtistDelele = (artist_id) => {
	fetch("/artists/" + artist_id, {
		method: "DELETE",
		body: {},
	}).then((response) => {
		console.log(response);
		window.location.replace("/artists");
	});
};
