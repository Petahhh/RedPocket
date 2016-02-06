var app = angular.module('redpocket', []);

app.controller('MainController', function($scope, $http) {

  var main = this;

  main.init = function () {
    $http.get('init/').then(
      function (response) {
        main.goals = JSON.parse(response.data.data.goals);
        main.chequing = response.data.data.chequing;
      }
    );
  };
  main.init();

  main.newGoal = function() {
    main.goals.push({
      name: main.new_goal_name,
      balance: 0,
      goal: main.new_goal_goal,
    });

    main.save();
  };

  main.save = function() {
    $http({
      method: "POST",
      url: "save",
      contentType: 'application/json; charset=utf-8',
      // data: {
      //   goals: JSON.stringify(main.goals),
      // }
      data: {"goals": main.goals},
    }).success(function (data) {
      console.log("success");
      console.log(data);
    })
    .error(function(data) {
      console.log("error");
      console.log(data);
    });
  };

  main.deleteGoal = function (name, $index) {
    main.goals.splice($index, 1);
    $http({
      method: "POST",
      url: "delete_goal",
      contentType: 'application/json; charset=utf-8',
      data: {"name": name},
    }).success(function (data) {
      console.log("success");
      console.log(data);
    })
    .error(function(data) {
      console.log("error");
      console.log(data);
    });

  }
})


  /* Added in for CSRF support. */
  .config(function ($httpProvider) {
    $httpProvider.defaults.headers.post['X-CSRFToken'] = $('input[name=csrfmiddlewaretoken]').val();
  });
