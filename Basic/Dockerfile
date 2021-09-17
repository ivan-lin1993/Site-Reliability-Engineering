FROM php:7.4-fpm

COPY ./app /var/www/html

WORKDIR /var/www/html

RUN chown -R www-data:www-data \
        /var/www/html/storage \
        /var/www/html/bootstrap/cache

EXPOSE 9000
CMD ["php-fpm"]
