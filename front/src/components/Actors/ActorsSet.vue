<template>
    <div>
      <div id="actors_title" class="col-3">Actor</div>
      <div id="actors_list">
          <span
          v-for="(actor, idx) in movie.actors.slice(0,4)"
          :key="idx"
          class="actors">
            <a id="actor_link" :href="'https://www.themoviedb.org/person/'+actor.id">
                {{actor.name}},
            </a>
          </span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
      name: 'ActorsSet',
      props: {
          movie:Object
      }
  }
  </script>
  
  <style>
    .actors {
      margin: 0px 5px;
      font-size: 18px;
      text-align: left;
    }

    #actors_title {
        width: 200px;
        height: 30px;
        text-align: center;
        font-size: 20px;
        margin-left: 5px;
        margin-top: 10px;
        margin-bottom: 10px;
        background-color: green;
        color: white;
        border-radius: 5px;
    }

    #actors_list {
        text-align: center;
    }

    #actor_link{
        text-decoration: none;
        color: black;
        font-weight: bold;
    }
  </style>