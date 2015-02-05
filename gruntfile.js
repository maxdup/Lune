module.exports = function(grunt) {
  grunt.initConfig({
    shell: {
      ressources: {
        command: 'pyside-rcc resources.qrc -py3 -o resources.py'
      }
    },
    watch: {
      styles: {
        files: ["views/qss/*.qss"],
        tasks: ['shell'],
        options: {
          livereload: true,
        }
      },
    },
  });
  grunt.loadNpmTasks('grunt-shell');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.registerTask('default', ['watch']);
};
