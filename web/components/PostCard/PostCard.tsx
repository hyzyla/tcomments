import React, { FC } from 'react'

import { Post } from '../../types'

interface Props {
    post: Post;
}

export const PostCard: FC<Props> = ({ post }) => {
    return (
        <div>
            <h1>{post.title}</h1>
            <p>{post.text}</p>
            <p>{post.date}</p>
        </div>
    )
};
