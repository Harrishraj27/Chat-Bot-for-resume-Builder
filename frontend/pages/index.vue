<template>
  <div>
    <h1>Resume Builder</h1>
    <QuestionForm />
  </div>
</template>

<script>
import QuestionForm from '~/components/QuestionForm.vue';

export default {
  components: {
    QuestionForm,
  },
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
}
h1 {
  color: #333;
}
</style>
