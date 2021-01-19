const form = d3.select('form')

const handleClick = () => {
    d3.event.preventDefault()

    // get user inputs
    let location = d3.select('#lat-long').property('value')
    let categories = d3.select('#categories').property('value')

}

d3.selectAll('#submit').on('click', handleClick)