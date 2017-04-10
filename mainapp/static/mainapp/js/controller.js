/**
 * Created by mykola.dekhtiarenko on 20.03.17.
 */

$(document).ready(function () {

var maininfo = $("#main-info");
$("#main-info-click").on("click", function (event) {
    $(".block").hide();
    maininfo.show();
});

var reports = $("#reports");
$("#reports-click").on("click", function (event) {
    $(".block").hide();
    reports.show();

});

var broadcasts = $("#broadcasts");
$("#broadcasts-click").on("click", function (event) {
    $(".block").hide();
    broadcasts.show();
});

var publishes = $("#publishes");
$("#publishes-click").on("click", function (event) {
     $(".block").hide();
    publishes.show();
});
var videos = $("#videos");
$("#videos-click").on("click", function (event) {
    $(".block").hide();
    videos.show();
});
var advmaterials = $("#advmaterials");
$("#advmaterials-click").on("click", function (event) {
    $(".block").hide();
    advmaterials.show();
});

$("#back-click").on("click", function (event) {
    window.location = "/redirect";
});

});