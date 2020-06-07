import React, { FC } from 'react'

import { Post as PostType } from '../../types'

interface Props {
    post: PostType;
}

export const Post: FC<Props> = ({ post }) => {
    return (
        <div>
            <h1>{post.title}</h1>
            <p>{post.text}</p>
            <p>{post.date}</p>
        </div>
    )
};
