function generate_keys() {
  $("#generate").prop("disabled", true);
  $("#generate").html("Generating keys...");
  $.getJSON("/gen_keys", function(data) {
    $("#master_key").text(data.master_key);
    $("#public_key").text(data.public_key);
  }).done(function() {
      $("#generate").html("Generate");
      $("#generate").prop("disabled", false);});
}
