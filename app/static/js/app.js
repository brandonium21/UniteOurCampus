// Declare app level module which depends on filters, and services
angular.module('Unite our campus', ['ngResource', 'ngRoute', 'ui.bootstrap', 'ui.date'])
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'views/register/register.html',
        controller: 'HomeController'})
      .when('/register', {
        templateUrl: 'views/register/register.html',
        controller: 'RegisterController'})
      .otherwise({redirectTo: '/'});
  }]);
