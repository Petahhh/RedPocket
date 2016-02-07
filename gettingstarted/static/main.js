$(document).foundation();
var app = angular.module('redpocket', []);

app.controller('MainController', function($scope, $http) {

  var main = this;

  $scope.show = false;
  $scope.show_new_goal = false;
  $scope.hovered_goal = -1;

  main.init = function () {
    $http.get('init/').then(
      function (response) {
        main.goals = JSON.parse(response.data.data.goals);
        main.chequing_balance = response.data.data.balance;
        main.pseudo_balance = response.data.data.balance;
        main.updatePseudoBalance();
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
    main.new_goal_name = "";
    main.new_goal_goal = "";
  };

  main.save = function() {
    $http({
      method: "POST",
      url: "save",
      contentType: 'application/json; charset=utf-8',
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
  };

  main.addToGoal = function(goal, $index) {
    goal.balance += parseInt(goal.addition);
    goal.addition = "";
    main.save();
    main.updatePseudoBalance();
    main.updateProgressBar($index);
  };

  main.updatePseudoBalance = function () {
    var pocketed = 0;
    for (var i = 0; i < main.goals.length; i++) {
      pocketed += main.goals[i].balance;
    }
    main.pseudo_balance = main.chequing_balance - pocketed;

  };

  main.updateProgressBar = function ($index) {
    var getPercent = ( main.goals[$index].balance / main.goals[$index].goal);
    var getProgressWrapWidth = $('.progress-wrap-' + $index).width();
    var progressTotal = getPercent * getProgressWrapWidth;
    var animationLength = getPercent * 1500;

    // on page load, animate percentage bar to data percentage length
    // .stop() used to prevent animation queueing
    $('.progress-bar-' + $index).stop().animate({
        left: progressTotal,
        easing: "linear",
    }, animationLength);
  };
});

/* Screen saver */
var mousetimeout;
var screensaver_active = true;
var idletime = 20;

function show_screensaver(){
    $('#screensaver').fadeIn();
    screensaver_active = true;
    screensaver_animation();
}

function stop_screensaver(){
    $('#screensaver').fadeOut();
    screensaver_active = false;
}

function getRandomColor() {
    var letters = '0123456789ABCDEF'.split('');
    var color = '#';
    for (var i = 0; i < 6; i++ ) {
        color += letters[Math.round(Math.random() * 15)];
    }
    return color;
}

$(document).mousemove(function(){

    clearTimeout(mousetimeout);
  
    if (screensaver_active) {
        stop_screensaver();
    }

    mousetimeout = setTimeout(function(){
        show_screensaver();
    }, 1000 * idletime); // 5 secs      
});

function screensaver_animation(){
    if (screensaver_active) {
        $('#screensaver').animate(
            {backgroundColor: getRandomColor()},
            400,
            screensaver_animation);
    }
}






