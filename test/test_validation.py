# -*- coding: utf-8 -*-

import ipaddress

from nose.tools import assert_true, assert_false

from nettool.nutility import NUtility as nu


class TestValidation(object):

    def setup(self):
        self.netmasks = [ipaddress.IPv4Interface(unicode('255.255.255.255/{0}'.format(x))).network.network_address.exploded for x in range(0, 33)]
        self.wildcards = [ipaddress.IPv4Interface(unicode('0.0.0.0/{0}'.format(x))).network.hostmask.exploded for x in range(0, 33)]

    def test_netmask_validation(self):
        for netmask in self.netmasks:
            assert_true(nu.validate.netmask(netmask))
        assert_false(nu.validate.netmask('netmask'))
        assert_false(nu.validate.netmask(33))

    def test_wildcard_validation(self):
        for wildcard in self.wildcards:
            assert_true(nu.validate.wildcard(wildcard))
        assert_false(nu.validate.wildcard('wildcard'))
        assert_false(nu.validate.wildcard(33))

    def test_prefix_validation(self):
        for wildcard in self.wildcards:
            assert_true(nu.validate.wildcard(wildcard))
        assert_false(nu.validate.wildcard('wildcard'))
        assert_false(nu.validate.wildcard(33))

    def test_host_validation(self):
        assert_false(nu.validate.host('host.example.com'))
        assert_false(nu.validate.host(''))
        assert_false(nu.validate.host('x' * 64))
        assert_false(nu.validate.host(':'))
        assert_false(nu.validate.host(20))
        assert_true(nu.validate.host('host'))

    def test_hostname_validation(self):
        assert_true(nu.validate.hostname('host.example.com'))
        assert_false(nu.validate.hostname(''))
        assert_false(nu.validate.hostname('x' * 64))
        assert_false(nu.validate.hostname(':'))
        assert_false(nu.validate.hostname(20))
        assert_true(nu.validate.hostname('host'))

    def test_ip_validation(self):
        assert_true(nu.validate.ip('1.2.3.4'))
        assert_true(nu.validate.ip(u'1.2.3.4'))
        assert_false(nu.validate.ip(u'256.2.3.4'))
        assert_false(nu.validate.ip('host'))
        assert_false(nu.validate.ip(''))
        assert_false(nu.validate.ip(1))

    def test_network_validation(self):
        assert_true(nu.validate.network('1.2.3.4/32'))
        assert_true(nu.validate.network('1.2.3.4/0'))
        assert_true(nu.validate.network('1.2.3.4'))
        assert_true(nu.validate.network(u'1.2.3.4'))
        assert_false(nu.validate.network(u'256.2.3.4'))
        assert_false(nu.validate.network('host'))
        assert_false(nu.validate.network(''))
        assert_false(nu.validate.network(1))