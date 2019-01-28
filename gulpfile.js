const gulp = require('gulp');
const pandoc = require('gulp-pandoc');
const browserSync = require('browser-sync');
const del = require('del');

function serve() {
    browserSync({
        server: {
            baseDir: './'
        }
    });

    gulp.watch('src/markdown/*.md', gulp.series(genPages));
    gulp.watch('pages/*.html', browserSync.reload);

}

function genPages() {
    return gulp.src('src/markdown/*')
        .pipe(pandoc({
            from: 'markdown',
            to: 'revealjs',
            ext: '.html',
            args: ['-i', '--slide-level=2', '-V', 'theme=solarized',
                '-V', 'revealjs-url=https://revealjs.com', '-s']
        }))
        .pipe(gulp.dest('pages'));
}

function clean() {
    return del(['pages']);
}

exports.build = gulp.series(clean, genPages);
exports.clean = gulp.series(clean);
exports.default = gulp.series(serve);
