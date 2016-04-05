// Declare app level module which depends on filters, and services
angular.module('Unite our campus', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html',
        controller: 'HomeController'})
      .when('/register', {
        templateUrl: 'views/register/register.html',
        controller: 'HomeController'})
      .otherwise({redirectTo: '/'});
  }]);

$(document).ready(function() {
    $('#fullpage').fullpage({
        menu: '#menu',
        sectionsColor: ['#122847', '#89cff0', '#FFFFFF', '#89cff0', '#122847', '#02898D'],
        anchors: ['firstpage', 'secondpage', 'thirdpage', 'fourthpage', 'fifthpage', 'sixthpage'],
        css3: true,
        scrollingSpeed: 800,
        verticalCentered: true
    });
    $(".firstpage").animate({"opacity":"1"}, 1500).delay(1000);
    $(".title").animate({"opacity":"1"}, 1500);
});