var app = angular.module('angularApp', ['ngRoute']);

app.config(['$routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: '/static/blog/js/views/test.html',
            controller: 'testController'
        })
}]);

