#! /usr/bin/env python3
'''Interpolation using Newton'''


def interp_coeffs(xvals, yvals):
    nbr_data_points = len(xvals)

    # sort inputs by xvals =>
    data = sorted(zip(xvals, yvals), reverse=False)
    xvals, yvals = zip(*data)

    depth = 1
    coeffs = [yvals[0]]
    iter_yvals = yvals

    while depth < nbr_data_points:

        iterdata = []

        for i in range(len(iter_yvals)-1):

            delta_y = iter_yvals[i+1]-iter_yvals[i]
            delta_x = xvals[i+depth]-xvals[i]
            iterval = (delta_y/delta_x)
            iterdata.append(iterval)

            # append top-most entries from table to coeffs =>
            if i == 0:
                coeffs.append(iterval)

        iter_yvals = iterdata
        depth += 1

    return(coeffs)


def interp_val(xvals, yvals):
    nbr_data_points = len(xvals)

    # sort inputs by xvals =>
    data = sorted(zip(xvals, yvals), reverse=False)
    xvals, yvals = zip(*data)

    depth = 1
    coeffs = [yvals[0]]
    iter_yvals = yvals

    while depth < nbr_data_points:

        iterdata = []

        for i in range(len(iter_yvals)-1):

            delta_y = iter_yvals[i+1]-iter_yvals[i]
            delta_x = xvals[i+depth]-xvals[i]
            iterval = (delta_y/delta_x)
            iterdata.append(iterval)

            # append top-most entries in tree to coeffs =>
            if i == 0:
                coeffs.append(iterval)

        iter_yvals = iterdata
        depth += 1

    def f(i):
        """
        Evaluate interpolated estimate at x.
        """
        terms = []
        retval = 0

        for j in range(len(coeffs)):

            iterval = coeffs[j]
            iterxvals = xvals[:j]
            for k in iterxvals:
                iterval *= (i-k)
            terms.append(iterval)
            retval += iterval
        return(retval)
    return(f)

x = [-1, 0, 3, 4]
y = [15.5, 3, 8, 1]
print(interp_coeffs(x, y))
