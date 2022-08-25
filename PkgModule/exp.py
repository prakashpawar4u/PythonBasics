# 1
# import example_pkg
#
# example_pkg.foo.foo_func()
# example_pkg.bar.bar_func()
# example_pkg.baz.baz_func()


#2
# from example_pkg import foo, bar, baz
# foo.foo_func()
# bar.bar_func()
# baz.baz_func()


#3
import example_pkg.foo as ex_foo
import example_pkg.bar as ex_bar
import example_pkg.baz as ex_baz
ex_foo.foo_func()
ex_bar.bar_func()
ex_baz.baz_func()

#https://towardsdatascience.com/whats-init-for-me-d70a312da583