var app = angular.module('CognitsApp', []);

app.controller('LandingCtrl', ['$scope', '$http', function($scope, $http) {

  $scope.sentMessage = false;
  $scope.message = { email: '', content: ''};

  $scope.sendMessage = function() {

    console.log("got call to sendMessage");
    $http.post('/send-message/', $scope.message).
      success(function(data, status, headers, config) {
        // this callback will be called asynchronously
        // when the response is available
        $scope.sentMessage = true;
      }).
      error(function(data, status, headers, config) {
        // called asynchronously if an error occurs
        // or server returns response with an error status.
      });


  };

}]);
