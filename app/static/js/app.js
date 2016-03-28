// Declare app level module which depends on filters, and services
angular.module('Unite our campus', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/home/home.html', 
        controller: 'HomeController'})
      .otherwise({redirectTo: '/'});
  }]);

$(document).ready(function() {
    $('#fullpage').fullpage({
        sectionsColor: ['#122847', '#89cff0', '#FFFFFF', '#FA6300'],
        css3: true,
        scrollingSpeed: 1000
    });
    $(".firstpage").animate({"opacity":"1"}, 1500).delay(1000);
    $(".title").animate({"opacity":"1"}, 1500);
});